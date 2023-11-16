def load_config(dataset_key='pilot', verbose=False):
    """Loads dictionary with path names and any other variables set through config.toml
    Args:
        verbose (bool, optional): print paths
    Returns:
        config: dict
    """
    import toml
    from pathlib import Path
    package_dir = Path(__file__).parent.parent.parent.absolute()
    config_file = package_dir / "config.toml"
    print(f'Paths are for dataset tagged: {dataset_key}')
    if verbose:
        print(f'package dir: {package_dir}')
        print(f'config file: {config_file}')
    
    config = dict()
    toml_dict = toml.load(config_file)
    config.update(toml_dict[dataset_key])
    config.update({'package_dir':package_dir,'config_file':config_file})
    not_found = []
    for key in config:
        if Path(config[key]).exists():
            config[key] = str(Path(config[key]))


    for key in not_found:
        print(f'Did not find {key}')
        config.pop(key, None)


    return config


def parse_filename(filename):
    """
    Parses a filename to extract the channel and zplanes information.
    if filename is C1-MAX_Stitch_A01_G001_25-35, 
    C1 is the channel and 25-35 are the zplanes
    
    Args:
    - filename (str): The name of the file to be parsed.
    
    Returns:
    - channel (str): The channel information extracted from the filename.
    - zplanes (str): The zplanes information extracted from the filename.
    """    
    
    channel = filename.split('-')[0]
    zplanes = filename.split('_')[-1].split('.')[0]
    return channel, zplanes