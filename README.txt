NAME
    grep

DESCRIPTION
    .. module:: grep
    .. moduleauthor:: Spronck Julien
    .. created:: Feb. 4, 2015
    .. modified::
    
    Python module to mimic the GNU grep function


VERSION
    1.0


VARIABLES
    ERROR_COLOR
    FILENAME_COLOR
    LINENB_COLOR
    MATCH_COLOR
    NORMAL


FUNCTIONS

    _get_all_files(files)
     |  Generator for recursively find files

    grep(pattern, file_pattern, ignore_case=False, line_number=True, no_file_name=False, count=False, files_with_matches=False, files_without_matches=False, only_matching=False, recursive=False, invert_match=False, line_regexp=False, group=None)
     |  grep searches the named input file_pattern for lines containing a match
     |  to the given pattern.  By default, grep prints the matching lines and
     |  returns an list of matching lines.
     |  
     |  pattern can be a regular expression understood by the Python re module.
     |  
     |  Args:
     |      pattern (str): the pattern to find. This can be a regular expression.
     |      file_pattern (str): the files in which to search the pattern. This
     |          can have wildcards.
     |      ignore_case (bool, optional): if True, search is case-insensitive.
     |          Defaults to False.
     |      line_number (bool, optional): if True, includes line number in results.
     |          Defaults to True.
     |      no_file_name (bool, optional): if True, does not include file names in
     |          the results. Defaults to False.
     |      count (bool, optional): if True, returns the number of matches per
     |          file rather than the matching lines. Defaults to False.
     |      files_with_matches (bool, optional): if True, returns a list of file
     |          names with matches. Defaults to False.
     |      files_without_matches (bool, optional): if True, returns a list of file
     |          names without matches. Defaults to False.
     |      only_matching (bool, optional): if True, returns only the matching part
     |          rather than entire line. Defaults to False.
     |      recursive (bool, optional): if True, search recursively under each
     |          directory. Defaults to False.
     |      invert_match (bool, optional): if True, returns the non-matching lines.
     |          Defaults to False.
     |      line_regexp (bool, optional): if True, returns only matches that match
     |          entire lines . Defaults to False.

    igrep(pattern, file_pattern, ignore_case=False, line_number=True, no_file_name=False, count=False, files_with_matches=False, files_without_matches=False, only_matching=False, recursive=False, invert_match=False, line_regexp=False, group=None)
     |  grep searches the named input file_pattern for lines containing a match
     |  to the given pattern.  By default, grep prints the matching lines and
     |  returns an list of matching lines.
     |  
     |  pattern can be a regular expression understood by the Python re module.
     |  
     |  Args:
     |      pattern (str): the pattern to find. This can be a regular expression.
     |      file_pattern (str): the files in which to search the pattern. This
     |          can have wildcards.
     |      ignore_case (bool, optional): if True, search is case-insensitive.
     |          Defaults to False.
     |      line_number (bool, optional): if True, includes line number in results.
     |          Defaults to True.
     |      no_file_name (bool, optional): if True, does not include file names in
     |          the results. Defaults to False.
     |      count (bool, optional): if True, returns the number of matches per
     |          file rather than the matching lines. Defaults to False.
     |      files_with_matches (bool, optional): if True, returns a list of file
     |          names with matches. Defaults to False.
     |      files_without_matches (bool, optional): if True, returns a list of file
     |          names without matches. Defaults to False.
     |      only_matching (bool, optional): if True, returns only the matching part
     |          rather than entire line. Defaults to False.
     |      recursive (bool, optional): if True, search recursively under each
     |          directory. Defaults to False.
     |      invert_match (bool, optional): if True, returns the non-matching lines.
     |          Defaults to False.
     |      line_regexp (bool, optional): if True, returns only matches that match
     |          entire lines . Defaults to False.


