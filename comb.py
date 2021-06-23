import subprocess
import itertools

file_list = []
for i in range(1, 11):
    fname = f"conll14/10gec_annotations/A{i}.m2"
    with open(fname) as infile:
        file_list.append(infile.read().split('\n\n'))

def bash_command(cmd):
    sp = subprocess.Popen(['/bin/bash', '-c', cmd], stdout=subprocess.PIPE)
    return sp.stdout.readlines()

def comb_score(n):
    F_list = []
    F_result = []
    # for i in range(10):
    #     cmd = f"./m2scorer conll14/official_submissions/AMU conll14/10gec_annotations/A{i+1}.m2"
    #     result = bash_command(cmd)
    #     # print(result)
    #     F0_5 = float(str(result[2]).split(': ')[1][:-3])
    #     F_list.append(F0_5)
    
    for t in list(itertools.combinations(range(1, 11), n)):
        with open(f"./combs/{'_'.join(map(str,t))}.m2", mode="w") as outfile:
            ts = []
            for line_index in range(len(file_list[0])):
                line_set = set()
                answer_list = []
                for i in t:
                    new_line_list = []
                    for line in file_list[i-1][line_index].split('\n'):
                        if len(line) > 0 and line[0] == 'A' and line[:-1] not in answer_list:
                            line = line[:-1] + str(t.index(i))
                        new_line_list.append(line)
                        answer_list.append(line[:-1])
                    line_set = line_set | set(new_line_list)
                sorted1 = sorted(line_set, reverse=True)
                sorted2 = sorted(sorted1[1:], key=lambda x:x[-1])
                ts.append(sorted1[:1] + sorted2)
            for line_set in ts:
                for line in line_set:
                    outfile.write(f"{line}\n")
                outfile.write("\n")

        # F_result.append(sum(t)/len(t))
    # print(F_result)
    # return sum(F_result)/len(F_result)

# print(comb_score(1))
comb_score(9)