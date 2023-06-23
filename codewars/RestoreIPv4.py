# https://www.codewars.com/kata/63a0f3f49547e9001e7ad1ca/python

class IPv4Address:
    # Good luck, have fun
    def __init__(self, parts):
        """
        Creates an object representing an IPv4 address

        :param parts: a list of 4 integers
        """
        if len(parts) != 4:
            raise ValueError('Should create IPv4Address when 4 valid integers provided')
        elif not all(isinstance(num, int) and num < 256 for num in parts):
            raise ValueError('Should not create IPv4Address with non-integer parts')
        elif parts[0] == 0:
            raise ValueError('Should not create IPv4Address with first part 0')
        # properly unmutable not working
        self._parts = tuple(parts)

    @classmethod
    def from_string(cls, string):
        return cls([int(num) for num in string.split('.')])

    def __eq__(self, other):
        if hasattr(other, 'parts'):
            raise ValueError("Shouldn't do 'less than' comparison between IPv4Address and object with 'parts' field")
        if isinstance(other, IPv4Address):
            return self._parts == other._parts
        return False

    def __hash__(self):
        return hash(tuple(self._parts))

    def __lt__(self, other):
        if hasattr(other, 'parts'):
            raise ValueError("Shouldn't do 'less than' comparison between IPv4Address and object with 'parts' field")
        if isinstance(other, IPv4Address):
            return self._parts < other._parts
        return NotImplemented

    def __gt__(self, other):
        if hasattr(other, 'parts'):
            raise ValueError("Shouldn't do 'greater than' comparison between IPv4Address and object with 'parts' field")
        if isinstance(other, IPv4Address):
            return self._parts > other._parts
        return NotImplemented

    def __le__(self, other):
        if hasattr(other, 'parts'):
            raise ValueError(
                "Shouldn't do 'less or equal than' comparison between IPv4Address and object with 'parts' field")
        if isinstance(other, IPv4Address):
            return self._parts <= other._parts
        return NotImplemented

    def __ge__(self, other):
        if hasattr(other, 'parts'):
            raise ValueError(
                "Shouldn't do 'greater or equal than' comparison between IPv4Address and object with 'parts' field")
        if isinstance(other, IPv4Address):
            return self._parts >= other._parts
        return NotImplemented

    def __str__(self):
        return '.'.join(str(num) for num in self._parts)


my_ip = IPv4Address([1, 1, 1, 255])
