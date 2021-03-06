"""
    Star Coordinates
"""

STAR_COORDINATES_ID = "Star Coordinates"

def star_coordinates(dimensional_values_df, axis_vectors_df, weights_df=None,
                     normalized_weights=False, normalization_method=None):
    """ Map points according to Star Coordinates setting
        dimensional_values_df: (pandas.Dataframe) product_id X dimensional_values
        axis_vectors_df: (pandas.Dataframe) vector_id X (x, y) components
        weights_df: (pandas.Dataframe) Weight value per vector
        [normalized_weights=False]: (Boolean) Normalize weights
        [normalization_method=None]: (func) Normalization method for weights
    """
    # TODO gchicafernandez - Add weights to the multiplication
    mapped_points = dimensional_values_df.dot(axis_vectors_df)
    mapped_points.columns = ['x', 'y']
    return mapped_points
