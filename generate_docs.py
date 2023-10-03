import os
from sphinx import build_main

def generate_docs():
    source_dir = 'docs'
    output_dir = 'docs/build'

    # Clean existing build
    if os.path.exists(output_dir):
        os.system(f'rm -r {output_dir}')

    # Generate documentation
    os.makedirs(output_dir)
    os.system(f'sphinx-quickstart {source_dir}')

    # Modify the configuration if needed (e.g., set project name)
    config_file = os.path.join(source_dir, 'conf.py')
    with open(config_file, 'a') as f:
        f.write('\nproject = "City Weather App"')

    # Build documentation
    build_main(argv=['sphinx-build', '-b', 'html', source_dir, output_dir])

if __name__ == '__main__':
    generate_docs()
