# Living People: Given a list of people with their birth and death years, implement a method to
# compute the year with the most number of people alive. You may assume that all people were born
# between 1900 and 2000 (inclusive). If a person was alive during any portion of that year, they should
# be included in that year's count. For example, Person (birth = 1908, death = 1909) is included in the
# counts for both 1908 and 1909.


class Person:
    def __init__(self, birth, death):
        self.birth = birth
        self.death = death


def find_min_birth_year(persons):
    min_birth_year = 2000
    for person in persons:
        min_birth_year = min(min_birth_year, person.birth)
    return min_birth_year


def find_max_death_year(persons):
    max_death_year = 1900
    for person in persons:
        max_death_year = max(max_death_year, person.death)
    return max_death_year

def find_persons_for_year(persons, year):
    count = 0
    for person in persons:
        if(year >= person.birth and year <= person.death):
            count += 1
    return count


if __name__ == '__main__':
    p1 = Person(1901, 1920)
    p2 = Person(1910, 1956)
    p3 = Person(1930, 1960)
    p4 = Person(1935, 1940)
    p5 = Person(1950, 2000)

    persons = [p1, p2, p3, p4, p5]

    start = find_min_birth_year(persons)
    end = find_max_death_year(persons)

    year_dict = {}
    for year in range(start, end+1):
        year_dict[year] = find_persons_for_year(persons, year)

    # find key (year) with max value (count) in year_dict
    max_count = max(year_dict.values())
    print(min([year for year in year_dict if year_dict[year] == max_count]))
    
