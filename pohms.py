import click

@click.group()
def main_cli():
	'''
		Ceramic-resistor/not-ceramic-resistor image dector
	'''
	pass

@main_cli.command()
def detect():
	'''
		Detect if an image is a ceramic resistor or not
	'''
	click.echo('potato')


if __name__ == '__main__':
	main_cli()