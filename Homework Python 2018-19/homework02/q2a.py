

import os, sys, json, re, prettytable, time

exercises = ['1', '2', '3']

def get_results(e):
    program    = "program0{}.py".format(e)
    noncompila = "program0{}.noncompila".format(e)
    tests_json = "program0{}.log.json".format(e)
    time_json  = "program0{}.tim.json".format(e)
    cc_json    = "program0{}.cyc.json".format(e)
    cog_json   = "program0{}.cog.json".format(e)
    result = {}
    if os.path.exists(program):
        if os.path.exists(noncompila):
            result['compiles'] = False
            return { e : result }
        else:
            result['compiles'] = True
        print('\t', e, 'compiles', result['compiles'])

        if os.path.exists(cc_json):
            with open(cc_json) as f:
                cyc = json.load(f)
            values = list(cyc.values())[0]
            ccs = map(lambda x: x['complexity'], values )
            result['cc']   = max(ccs)
            print('\t', e, 'cc', result['cc'])
        else:
            print(cc_json, 'non esiste')

        if False:
            if os.path.exists(cog_json):
                with open(cog_json) as f:
                    cog = json.load(f)
                result['cog']   = cog['max']
                print('\t', e, 'cog', result['cog'])
            else:
                print(cog_json, 'non esiste')

        passed = False
        if os.path.exists(tests_json):
            with open(tests_json) as f:
                tests = json.load(f)
            result['passed']   = tests['report']['summary'].get('passed',0)
            result['numtests'] = tests['report']['summary']['num_tests']
            print('\t', e, 'passed', result['passed'], 'numtests', result['numtests'])
            passed = result['passed'] == result['numtests']
        else:
            print(tests_json, 'non esiste')

        if os.path.exists(time_json) and passed:
            with open(time_json) as f:
                t = json.load(f)
            result['time']   = round(t['time'], 5)
            print('\t', e, 'time', result['time'])
        else:
            print(time_json, 'non esiste')

    return { e : result }


multipliers = { 'msec': 1,
                'sec' : 1e3,
                'usec': 1e-3,
            }

pattern = re.compile("[0-9]+ loops, best of [0-9]+: ([0-9.]+) (.?sec) per loop")

def get_time(filename):
    result = {}
    with open(filename) as f:
        for line in f:
            match = re.search(pattern, line)
            if match:
                #print(match.groups())
                t, sec = match.groups()
                #print(time, sec)
                t = float(t)
                t *= multipliers[sec]
                result['time'] = t
                print(result)
    with open(filename + '.json', mode='w') as fj:
        json.dump(result, fj, indent=2)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_time(sys.argv[1])
    elif len(sys.argv) == 1:
        result = {}
        for e in exercises:
            result.update(get_results(e))
        #result['date'] = time.asctime()
        result['date'] = time.time()
        with open('Q2A.json', mode='w') as fj:
            json.dump(result, fj, indent=2)
    else:
        print("""Usage:
        Q2A.py filename.tim     to produce filename.tim.json
        Q2A.py                  to produce Q2A.json
        """)
