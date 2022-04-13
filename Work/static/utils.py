import sys
import os
sys.path.insert(1, os.getcwd())



def get_commit_code_fromGH(Rcsvpath = 'Project_link.csv', code_path = "Demo"):
    '''
    This function is used to get the commit code from github.
    The names of the files, states of the files before/after commit, hunk number, line number, names of the called functions, word number can be useful for the future.
    '''
    g, backup_keys, no_bused_key, accesskey = initialize_G()

    with open(Rcsvpath,"rU") as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"', dialect=csv.excel_tab)
        data_read = [row for row in reader]
        load_object = 0
        for idx, line in enumerate(data_read):

            commit_ids = line[-1].split("::")
            commit_ids = [ids for ids in commit_ids if ids]
            repository = line[0].replace('https://api.github.com/repos/', '')
            user_name, repo_name = repository.split("/")
            pull_request_id = line[1]
            try:
                repo = g.get_repo(repository)
            except Exception as e:
                print("Repo not found")
                print(e)
                continue
            g, no_bused_key, load_object = changeG(g, accesskey, backup_keys, no_bused_key, load_object)
            if load_object:
                repo = g.get_repo(repository)
                print("New G loaded")
                load_object = 0
            for commit_id in commit_ids:
                try:
                    commit = repo.get_commit(sha=commit_id)
                    for file_id, changes in enumerate(commit.files):
                        if changes.patch is not None:
                            hunks = changes.patch.split("\n@@")
                            for hunk_id, hunk in enumerate(hunks):
                                added_lines = []
                                deleted_lines = []
                                code_lines = hunk.split("\n")
                                for code_line in code_lines:
                                    if code_line.startswith('+'):
                                        added_lines.append(code_line)
                                    elif code_line.startswith('-'):
                                        deleted_lines.append(code_line)
                                    else:
                                        continue
                                if not os.path.exists(code_path+"/Codes/"+user_name+"::"+repo_name+"/"+pull_request_id+"/"+commit_id+"/f"+str(file_id)+"/h"+str(hunk_id)):
                                    os.makedirs(code_path+"/Codes/"+user_name+"::"+repo_name+"/"+pull_request_id+"/"+commit_id+"/f"+str(file_id)+"/h"+str(hunk_id))
                                with open(code_path+"/Codes/"+user_name+"::"+repo_name+"/"+pull_request_id+"/"+commit_id+"/f"+str(file_id)+"/filename", "w") as fp0:
                                    fp0.write("".join(changes.filename))
                                with open(code_path+"/Codes/"+user_name+"::"+repo_name+"/"+pull_request_id+"/"+commit_id+"/f"+str(file_id)+"/h"+str(hunk_id)+"/added", "w") as fp1:
                                    fp1.write("\n".join(added_lines))
                                with open(code_path+"/Codes/"+user_name+"::"+repo_name+"/"+pull_request_id+"/"+commit_id+"/f"+str(file_id)+"/h"+str(hunk_id)+"/deleted", "w") as fp2:
                                    fp2.write("\n".join(deleted_lines))
                        else:
                            continue
                except Exception as e:
                    print("Commit not found")
                    print(e)
                    continue

# get_commit_code_fromGH('projectWise_data_from_github/Ansible_backport_in_TitleandLabes_PRs.csv',
#  'data_code')