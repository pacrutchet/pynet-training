import yaml, json
import sys

def dump():
    my_list = range(5)
    my_list.append('entry 2')
    my_list.append('entry 3')
    my_list.append({})
    my_list[-1]['key1'] = 'value1'
    my_list[-1]['key2'] = range(5)

    with open("list.yml", "w") as f:
        f.write(yaml.dump(my_list, default_flow_style=False))

    f.close()

    with open("list.json", "w") as f:
        json.dump(my_list, f)

    f.close()

def load():
    with open("list.yml") as f:
        new_list_yaml = yaml.load(f)

    f.close()

    with open("list.json") as f:
        new_list_json = json.load(f)
    f.close()

    print "######YAML#####\n"
    print new_list_yaml
    print "######JSON#####\n"
    print new_list_json

if __name__ == "__main__":
    print len(sys.argv)
    if len(sys.argv) == 2:
        if sys.argv[1] == "load":
            load()
        elif sys.argv[1] == "dump":
            dump()

