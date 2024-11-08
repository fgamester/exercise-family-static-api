
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name ):
        self.last_name = last_name
        self._nextid = 1
        # example list of members
        self._members = [
            {
            'id': self._generateId(),
            'first_name': 'John',
            'last_name': self.last_name,
            'age': 33,
            'lucky_numbers': [7, 13, 22]
        },
            {
            'id': self._generateId(),
            'first_name': 'Jane',
            'last_name': self.last_name,
            'age': 35,
            'lucky_numbers': [10, 14, 3]
        },
            {
            'id': self._generateId(),
            'first_name': 'Jimmy',
            'last_name': self.last_name,
            'age': 5,
            'lucky_numbers': [1]
        },
        ]

    def _generateId(self):
        generated_id = self._nextid
        self._nextid += 1
        return generated_id

    def add_member(self, member):
        if 'id' not in member:
            member['id']=self._generateId()
        member['last_name']=self.last_name
        self._members.append(member)
        pass

    def delete_member(self, id):
        self._members = [member for member in self._members if member['id'] != id]

    def get_member(self, id):
        member = next((member for member in self._members if member['id'] == id), None)
        return member

    def get_all_members(self):
        return self._members
