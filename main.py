import os 
import fiona
import logging
import pathlib
import rasterio as rio
import geopandas as gpd

# ------LOGGING------
# Allows us to get some useful information about how the script has run and the issues that arose.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('logfile.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
# ------        ------


def removeSpikes(spiky_layer):
    """Remove the spikes from the polygons.
    
    Keyword arguments:
    spiked_poly -- The gpkg file which needs to removed of spikes
    Return: return a .gpkg that has had the faulty spikes removed.
    """
    # Check if the geometry is valid.
    for geo in spiky_layer['geometry']:
        if geo.is_valid == True:
            print("The polygon is valid and requires no processing")
            logger.info("The polygon is valid and requires no processing")
        elif geo.is_valid() == False:
            # TODO: Add the processing which will remove the spikes from the polygon
            pass
        else:
            print("The validity of the polygon is unknown, check the source")
            logger.warning("The validity of the polygon is unknown, check the source")
    
    return fixed_poly


def main(spiky_layer):
    """Run the process to remove the spikes form the gpkg file and export the final output.
    
    Keyword arguments:
    GeoPackage -- The data to be processed (the varaiable containing the read in data of the gpkg file)
    Return: None
    """
    # Check for output dir/Create output dir
    out_dir = r"./output/"
    if not pathlib.Path(out_dir).exists():
        pathlib.Path(out_dir).mkdir(parents=True, exist_ok=True)

    # Run the function to remove the spikes form the gpkg file
    no_spikes = removeSpikes(spiky_layer)
    
    # Write out the output to output dir
    # TODO write out the fixed polygons (var no_spikes) into the output folder 
    
    return


if __name__ == '__main__':
    
    # TODO: Use the os package to read the folder structure and look for the "data" folder, that will be var to loop through. check old code.
    
    # Read in the .gpkg file from the "data" folder
    spiky_layer = gpd.read_file(r"C:\Users\USER\Documents\Kartoza-test\data\spiky-polygons.gpkg")
    
    main(spiky_layer)
    print("Job complete")
    logger.info("--- Job complete ---")