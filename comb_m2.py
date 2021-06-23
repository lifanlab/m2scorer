import subprocess
import itertools
import sys

def bash_command(cmd):
    sp = subprocess.Popen(['/bin/bash', '-c', cmd], stdout=subprocess.PIPE)
    return sp.stdout.readlines()

def comb_score(n):
    n = int(n)
    F_list = []
    for i in list(itertools.combinations(range(1, 11), n)):
        cmd = f"./m2scorer conll14/BEA-hinative-coll ./combs{n}/{'_'.join(map(str,i))}.m2"
        result = bash_command(cmd)
        print(result)
        F0_5 = float(str(result[2]).split(': ')[1][:-3])
        F_list.append(F0_5)
    return sum(F_list)/len(F_list)

print(comb_score(sys.argv[1]))