"""
python main.py <arg1> <arg2>
"""
import typer

def main(first_name: str, last_name: str):
    typer.echo(f"Hello {first_name} {last_name}")


if __name__ == "__main__":
    typer.run(main)
