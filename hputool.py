import numpy as np

# Convert tran style to parser style of Coll2003 dataset
def convert_coll_dataset(fin, fout):
        file = open(fout, "w")
        for line in open(fin):
            sentence, actions = map(lambda x: x.strip().split(), line.strip().split('|||'))
            stack_state, buffer_state = [], sentence
            
            file.write('\n')
            for action in actions:
                file.write('{}{}\n'.format(str(stack_state), str(buffer_state)))
                if action[0] == 'O':
                        assert len(stack_state) == 0
                        buffer_state = buffer_state[1:]
                elif action[0] == 'S':
                        stack_state.append(buffer_state[0])
                        buffer_state = buffer_state[1:]
                elif action[0] == 'R':
                        stack_state = []
                file.write('{}\n'.format(action))
        assert len(stack_state) == 0 and len(buffer_state) == 0
        file.write('{}{}\n'.format(str(stack_state), str(buffer_state)))
        file.close()
        
# Convert Coll2003's standard style to parser style of Coll2003 dataset
def convert_coll2standard(fin, fout):
        file = open(fout, "w")
        for line in open(fin):
            sentence, actions = map(lambda x: x.strip().split(), line.strip().split('|||'))
            stack_state, buffer_state = [], sentence
            
            file.write('\n')
            for action in actions:
                file.write('{}{}\n'.format(str(stack_state), str(buffer_state)))
                if action[0] == 'O':
                        assert len(stack_state) == 0
                        buffer_state = buffer_state[1:]
                elif action[0] == 'S':
                        stack_state.append(buffer_state[0])
                        buffer_state = buffer_state[1:]
                elif action[0] == 'R':
                        stack_state = []
                file.write('{}\n'.format(action))
        assert len(stack_state) == 0 and len(buffer_state) == 0
        file.write('{}{}\n'.format(str(stack_state), str(buffer_state)))
        file.close()