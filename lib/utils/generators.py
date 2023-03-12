"""Generators to cycle through docmodels, and get data based on specific filters and/or properties"""

import os
import pickle
from typing import Callable, Optional, Iterable
from lib.nlp_params import TT_NVA_TAGS
from lib.docmodel import DocModel

def generate_docmodels_from_paths(path_list: Iterable, vocal: bool = True, filter_fct: Optional[Callable] = None):
    """Base generator, yields DocModels based on a list of pickled docmodels paths.

    Args:
        path_list: A list of pickled DocModel paths, can be generated by calling os.listdir on docmodels_path
        vocal: Whether to to print each time 5k docmodels are generated
        filter_fct: None or a function taking a docmodel as argument and returning a bool. Only docmodels for which the function returns true will be yielded.

    Returns:

    """

    i = 0
    for path in path_list:
        with open(path, 'rb') as f:
            try:
                dm = pickle.load(f)
                if (filter_fct is None) or filter_fct(dm):
                    i += 1
                    if vocal and i % 5000 == 0:
                        print(f'Generated {i} docmodels')
                    yield dm
            except EOFError:
                print(f'ERROR! Could not open docmodel at: {path}')


def generate_ids_tags(path_list, function_name, flatten=True,
                      dms_filter_fct: Optional[Callable] = None, tags_filter_fct: Optional[Callable] = None):
    for dm in generate_docmodels_from_paths(path_list, filter_fct=dms_filter_fct):
        if flatten:
            yield dm.get_id(), [tag for tag in getattr(dm, function_name)(flatten=flatten)
                                if tags_filter_fct is None or tags_filter_fct(tag)]
        else:
            for i, para in enumerate(getattr(dm, function_name)(flatten=flatten)):
                yield f'{dm.get_id()}_{i}', [tag for tag in para if tags_filter_fct is None or tags_filter_fct(tag)]


# Shortcut generators below, based on those defined above but tuned to yield the data used in the analyses
# dir_path param should always be the path to the folder containing the pickled docmodels (and nothing else)

def generate_all_docmodels(dir_path):
    """Shortcut to generate all docmodels in a dir. All files must be DocModels"""

    return generate_docmodels_from_paths(dir_path / f for f in os.listdir(dir_path))


def generate_ids_abs_tags(dir_path, flatten=True):
    """Generator yielding (id, [tags]) pairs, for abstract tags.

    Args:
        dir_path: DocModel dir
        flatten: Wheter to flatten the paragraphs. If false, will yield paragraphs with id [doc_id]_[para_num]

    Returns:

    """

    return generate_ids_tags([dir_path / f for f in os.listdir(dir_path)], 'get_abs_tags', flatten=flatten)


def generate_ids_text_tags(dir_path, flatten=True):
    """Generator yielding (id, [tags]) pairs, for text tags.

        Args:
            dir_path: DocModel dir
            flatten: Wheter to flatten the paragraphs. If false, will yield paragraphs with id [doc_id]_[para_num]

        Returns:

        """

    return generate_ids_tags([dir_path / f for f in os.listdir(dir_path)], 'get_text_tags', flatten=flatten)


def generate_ids_text_tags_filtered(dir_path, filter_fct, flatten=True):
    """ Generator yielding (id, [tags]) pairs, for text tags filtered on a specified condition.

    Args:
        dir_path:
        filter_fct: function filtering tags, should take a tag and return a bool
        flatten:

    """

    return generate_ids_tags([dir_path / f for f in os.listdir(dir_path)], 'get_text_tags', flatten=flatten, tags_filter_fct=filter_fct)


