"""
Testing for textpipe pipeline.py
"""

from textpipe.pipeline import Pipeline

TEXT = 'Test sentence for testing'
PARAMS_DUMMY = {'foo':'bar', 'bar':'foo'}
PARAMS_CLEAN_TEXT = {'clean_html':True}
PIPELINE = [('raw', PARAMS_DUMMY),
            ('nwords', PARAMS_DUMMY),
            ('complexity', PARAMS_DUMMY),
            ('clean_text', PARAMS_CLEAN_TEXT)]
PIPE = Pipeline(PIPELINE)


def test_return_dict():
    """
    The returned dictionary should have the same length as the pipeline
    """
    assert len(PIPE(TEXT)) == len(PIPELINE)
