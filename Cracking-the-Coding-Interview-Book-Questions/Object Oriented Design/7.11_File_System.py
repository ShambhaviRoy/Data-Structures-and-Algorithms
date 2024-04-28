# File System: Explain the data structures and algorithms that you would use to design an in-memory
# file system. Illustrate with an example in code where possible.


from abc import ABC, abstractmethod
from datetime import datetime

class Entry(ABC):
    def __init__(self, name, directory):
        self.name = name
        self.parent = directory
        self.created = datetime.now()
        self.last_accessed = datetime.now()
        self.last_updated = datetime.now()

    @abstractmethod
    def get_size(self, entry):
        pass

    def get_full_path_name(self):
        if(not self.parent):
            return self.name
        return self.parent.get_full_path_name() + '/' + self.name
    
    def delete(self):
        if(not self.parent):
            return False
        return self.parent.delete_entry(self)
    


class File(Entry):
    def __init__(self, name, directory, size):
        super().__init__(name, directory)
        self.size = size

    def get_size(self):
        return self.size




class Directory(Entry):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.content = []
    
    def get_size(self):
        total_size = 0
        for content in self.content:
            total_size += content.size
        return total_size
    

    def get_number_of_files(self):
        file_counter = 0
        for content in self.content:
            if(isinstance(content, Directory)):
                file_counter += content.get_number_of_files
            else:
                file_counter += 1
        return file_counter
   

    
    def add_entry(self, entry):
        self.content.append(entry)

    def delete_entry(self, entry):
        return self.content.remove(entry.name)

                

if __name__ == "__main__":
    home = Directory('home', None)
    dir1 = Directory('dir1', home)
    dir2 = Directory('dir2', dir1)
    
    file1 = File('file1', dir2, 10)
    file2 = File('file2', dir2, 20)

    dir2.content = [file1, file2]

    print(dir2.get_size())
    print(dir2.get_number_of_files())
    print(file2.get_full_path_name())






