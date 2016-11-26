# Module Imports
import datetime
import sys
import lumbercalc.benches
import json

# Main Function
def run(args):

    # Initialize Run Timer
    time_start = datetime.datetime.now()
  
    # Masthead
    version = '0.1'

    if args.verbose:
        content = [
            'LumberCalc: The Material Costs Calculator',
            'Kenneth P. J. Dyer',
            'kenneth@avoceteditors.com',
            'Version: %s' % version, '']
        masthead = '\n  '.join(content)
    else:
        masthead = 'LumberCalc - version %s' % version
    print(masthead)

    # Load Prices
    try:
        f = open(args.prices, 'r')
        data = json.load(f)
        f.close()
    except:
        raise SyntaxError("Unable to open price file: %s" % args.prices)

    # Projects
    projects = {
        "sawbench": lumbercalc.benches.Sawbench
    }

    # Exit
    time_end = datetime.datetime.now()
    time_diff = time_end - time_start
    sec = round(time_diff.total_seconds(), 2)
    close_msg = 'Operation completed in %s seconds' % sec
    print(close_msg)
    sys.exit(0)
