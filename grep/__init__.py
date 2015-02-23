'''
.. module:: grep
.. moduleauthor:: Spronck Julien
.. created:: Feb. 4, 2015
.. modified::

Python module to mimic the GNU grep function
'''

__version__ = '1.0'

LINENB_COLOR = ''
FILENAME_COLOR = ''
ERROR_COLOR = ''
MATCH_COLOR = ''
NORMAL = ''
try:
    from grepconfig import *
except ImportError:
    pass

def _get_all_files(files):
    '''
    Generator for recursively find files
    '''
    import os
    for fil in files:
        if os.path.isdir(fil):
            for root, _, filenames in os.walk(fil):
                for filename in filenames:
                    yield os.path.join(root, filename)
        else:
            yield fil

def grep(pattern, file_pattern, ignore_case=False, line_number=True,
         no_file_name=False, count=False, files_with_matches=False,
         files_without_matches=False, only_matching=False, recursive=False,
         invert_match=False, line_regexp=False, group=None):
    '''
    grep searches the named input file_pattern for lines containing a match
    to the given pattern.  By default, grep prints the matching lines and
    returns an list of matching lines.

    pattern can be a regular expression understood by the Python re module.

    Args:
        pattern (str): the pattern to find. This can be a regular expression.
        file_pattern (str): the files in which to search the pattern. This
            can have wildcards.
        ignore_case (bool, optional): if True, search is case-insensitive.
            Defaults to False.
        line_number (bool, optional): if True, includes line number in results.
            Defaults to True.
        no_file_name (bool, optional): if True, does not include file names in
            the results. Defaults to False.
        count (bool, optional): if True, returns the number of matches per
            file rather than the matching lines. Defaults to False.
        files_with_matches (bool, optional): if True, returns a list of file
            names with matches. Defaults to False.
        files_without_matches (bool, optional): if True, returns a list of file
            names without matches. Defaults to False.
        only_matching (bool, optional): if True, returns only the matching part
            rather than entire line. Defaults to False.
        recursive (bool, optional): if True, search recursively under each
            directory. Defaults to False.
        invert_match (bool, optional): if True, returns the non-matching lines.
            Defaults to False.
        line_regexp (bool, optional): if True, returns only matches that match
            entire lines . Defaults to False.
    '''

    import glob
    import os
    import re

    files = glob.iglob(file_pattern)
    if recursive:
        files = _get_all_files(files)

    nfiles = 0

    out = []

    flags = 0 if not ignore_case else re.IGNORECASE
    if line_regexp:
        pattern = '(^{0}$)'.format(pattern)
        flags = flags | re.MULTILINE

    for fil in files:
        if os.path.isdir(fil):
            # file is a directory
            print ERROR_COLOR + '{0}: Is a directory'.format(fil)
            continue
        nfiles += 1
        nmatches = 0
        with open(fil, 'r') as fichier:
            ## Loop through files
            if line_number:
                line_nb = 0          ## Initialize line number

            for line in fichier:
                ## Loop through lines of each file
                if line_number:
                    line_nb += 1     ## Increment line number

                match = re.search(pattern, line, flags=flags)
                if match and not invert_match:
                    ## A pattern was found
                    if files_with_matches:
                        out.append(fil)
                        print FILENAME_COLOR + fil
                        break
                    nmatches += 1
                    if files_without_matches:
                        break
                    cprefix = NORMAL
                    prefix = ''
                    if line_number:
                        ## Print line number
                        cprefix = LINENB_COLOR + '{0:4}:'.format(line_nb) + cprefix
                        prefix = '{0:4}:'.format(line_nb) + prefix
                    if not no_file_name and not os.path.isfile(file_pattern):
                        ## Print file name
                        cprefix = FILENAME_COLOR + '{0:24}:'.format(fil) + cprefix
                        prefix = '{0:24}:'.format(fil) + prefix
                    if not count:
                        if group != None:
                            out.append(prefix + match.group(group))
                            cout = cprefix + match.group(group)
                        elif only_matching:
                            out.append(prefix + match.group(0))
                            cout = cprefix + match.group(0)
                        else:
                            the_line = line.rstrip('\n')
                            beg = the_line[:match.start()]
                            end = the_line[match.end():]
                            mat = match.group(0)
                            out.append(prefix + line.rstrip('\n'))
                            cout = cprefix + NORMAL + beg + MATCH_COLOR + mat + NORMAL + end
                        print cout
                elif not match and invert_match:
                    cprefix = NORMAL
                    prefix = ''
                    nmatches += 1
                    if line_number:
                        ## Print line number
                        cprefix = LINENB_COLOR + '{0:4}:'.format(line_nb) + cprefix
                        prefix = '{0:4}:'.format(line_nb) + prefix
                    if not no_file_name and not os.path.isfile(file_pattern):
                        ## Print file name
                        cprefix = FILENAME_COLOR + '{0:24}:'.format(fil) + cprefix
                        prefix = '{0:24}:'.format(fil) + prefix
                    if not count:
                        out.append(prefix + line.rstrip('\n'))
                        print cprefix + line.rstrip('\n')
            if files_without_matches and nmatches == 0:
                out.append(fil)
                print FILENAME_COLOR + fil
        if count and not files_without_matches:
            cprefix = NORMAL
            prefix = ''
            if not no_file_name and not os.path.isfile(file_pattern):
                ## Print file name
                cprefix = FILENAME_COLOR + '{0:24}:'.format(fil)
                prefix = '{0:24}:'.format(fil)
            out.append('{0}{1}'.format(prefix, nmatches))
            print '{0}{1}'.format(cprefix, nmatches)

    if nfiles == 0:
        # No files correspond to given pattern
        print ERROR_COLOR + '{0}: No such file or directory'.format(file_pattern)
        return

    return out

def igrep(pattern, file_pattern, ignore_case=False, line_number=True,
         no_file_name=False, count=False, files_with_matches=False,
         files_without_matches=False, only_matching=False, recursive=False,
         invert_match=False, line_regexp=False, group=None):
    '''
    grep searches the named input file_pattern for lines containing a match
    to the given pattern.  By default, grep prints the matching lines and
    returns an list of matching lines.

    pattern can be a regular expression understood by the Python re module.

    Args:
        pattern (str): the pattern to find. This can be a regular expression.
        file_pattern (str): the files in which to search the pattern. This
            can have wildcards.
        ignore_case (bool, optional): if True, search is case-insensitive.
            Defaults to False.
        line_number (bool, optional): if True, includes line number in results.
            Defaults to True.
        no_file_name (bool, optional): if True, does not include file names in
            the results. Defaults to False.
        count (bool, optional): if True, returns the number of matches per
            file rather than the matching lines. Defaults to False.
        files_with_matches (bool, optional): if True, returns a list of file
            names with matches. Defaults to False.
        files_without_matches (bool, optional): if True, returns a list of file
            names without matches. Defaults to False.
        only_matching (bool, optional): if True, returns only the matching part
            rather than entire line. Defaults to False.
        recursive (bool, optional): if True, search recursively under each
            directory. Defaults to False.
        invert_match (bool, optional): if True, returns the non-matching lines.
            Defaults to False.
        line_regexp (bool, optional): if True, returns only matches that match
            entire lines . Defaults to False.
    '''

    import glob
    import os
    import re

    files = glob.iglob(file_pattern)
    if recursive:
        files = _get_all_files(files)

    nfiles = 0

    flags = 0 if not ignore_case else re.IGNORECASE
    if line_regexp:
        pattern = '(^{0}$)'.format(pattern)
        flags = flags | re.MULTILINE

    for fil in files:
        if os.path.isdir(fil):
            # file is a directory
            print ERROR_COLOR + '{0}: Is a directory'.format(fil)
            continue
        nfiles += 1
        nmatches = 0
        with open(fil, 'r') as fichier:
            ## Loop through files
            if line_number:
                line_nb = 0          ## Initialize line number

            for line in fichier:
                ## Loop through lines of each file
                if line_number:
                    line_nb += 1     ## Increment line number

                match = re.search(pattern, line, flags=flags)
                if match and not invert_match:
                    ## A pattern was found
                    if files_with_matches:
                        yield FILENAME_COLOR + fil
                        #print FILENAME_COLOR + fil
                        break
                    nmatches += 1
                    if files_without_matches:
                        break
                    prefix = ''
                    if line_number:
                        ## Print line number
                        prefix = '{0:4}:'.format(line_nb) + prefix
                    if not no_file_name and not os.path.isfile(file_pattern):
                        ## Print file name
                        prefix = '{0:24}:'.format(fil) + prefix
                    if not count:
                        if group != None:
                            yield prefix + match.group(group)
                        elif only_matching:
                            yield prefix + match.group(0)
                        else:
                            yield prefix + line.rstrip('\n')
                elif not match and invert_match:
                    prefix = ''
                    nmatches += 1
                    if line_number:
                        ## Print line number
                        prefix = '{0:4}:'.format(line_nb) + prefix
                    if not no_file_name and not os.path.isfile(file_pattern):
                        ## Print file name
                        prefix = '{0:24}:'.format(fil) + prefix
                    if not count:
                        yield prefix + line.rstrip('\n')
            if files_without_matches and nmatches == 0:
                yield fil
                print FILENAME_COLOR + fil
        if count and not files_without_matches:
            prefix = ''
            if not no_file_name and not os.path.isfile(file_pattern):
                ## Print file name
                prefix = '{0:24}:'.format(fil)
            yield '{0}{1}'.format(prefix, nmatches)

    if nfiles == 0:
        # No files correspond to given pattern
        print ERROR_COLOR + '{0}: No such file or directory'.format(file_pattern)
