import typer
import http.server
import socketserver
import os
from pathlib import Path
from typing import Optional

app = typer.Typer(
    help="WebCat - HTTP Server Toolkit for Red Teamers",
    context_settings={"help_option_names": ["-h", "--help"]}
)

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def LogMessage(self, format, *args):
        typer.echo(f"[{self.address_string()}] {format % args}")

    def do_GET(self):
        # Log the request before processing
        typer.echo(f"[GET] {self.path} from {self.client_address[0]}")

        # Handle the request only once
        try:
            super().do_GET()
        except (BrokenPipeError, ConnectionResetError):
            # Client disconnected - this is normal, just log it quietly
            typer.echo(f"[INFO] Client disconnected during transfer: {self.client_address[0]}")

    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)

            typer.echo(f"[POST] {self.path} from {self.client_address[0]}")
            typer.echo(f"    Data Length: {content_length} bytes")

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Data Received\n")
        except (BrokenPipeError, ConnectionResetError):
            typer.echo(f"[INFO] Client disconnected during POST: {self.client_address[0]}")


@app.command()
def server(
    port: int = typer.Option(8000, "--port", "-p", help="Port to listen on"),
    directory: str = typer.Option(".", "--directory", "-d", help="Directory to serve"),
    bind: str = typer.Option("0.0.0.0", "--bind", "-b", help="IP address to bind to")
):
    dir_path = Path(directory)
    if not dir_path.exists():
        typer.secho(f"[ERROR] Directory '{directory}' does not exist", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)

    os.chdir(directory)
    directory_path = dir_path.resolve()

    typer.secho("Starting WebCat HTTP Server...", fg=typer.colors.BRIGHT_GREEN, bold=True)
    typer.echo(f"   Serving: {directory_path}")
    typer.secho(f"   Listening on: http://{bind}:{port}", fg=typer.colors.CYAN)
    typer.echo(f"   Press Ctrl+C to stop\n")

    try:
        with socketserver.TCPServer((bind, port), CustomHTTPRequestHandler) as httpd:
            httpd.allow_reuse_address = True
            httpd.serve_forever()
    except KeyboardInterrupt:
        typer.secho("\nShutting Down Server...", fg=typer.colors.YELLOW)
    except PermissionError:
        typer.secho(f"[ERROR] Permission Denied. Port {port} requires root privileges!", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)

def version_callback(value: bool):
    if value:
        typer.echo("WebCat version v0.1.0")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(None, "--version", "-v", callback=version_callback, is_eager=True)
):
    pass

if __name__ == "__main__":
    app()