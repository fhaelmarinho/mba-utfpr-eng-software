class Identifier:
    def validate_identifier(self, s: str) -> bool:
        # Lança IndexError para string vazia (equivalente ao StringIndexOutOfBoundsException do Java)
        if not s:
            raise IndexError("string index out of range")
        
        achar = s[0]
        valid_id = self.valid_s(achar)
        
        if len(s) > 1:
            achar = s[1]
            i = 1
            while i < len(s) - 1:
                achar = s[i]
                if not self.valid_f(achar):
                    valid_id = False
                i += 1

        if valid_id and (1 <= len(s) < 6):
            return True
        else:
            return False

    def valid_s(self, ch: str) -> bool:
        if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
            return True
        else:
            return False

    def valid_f(self, ch: str) -> bool:
        if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z') or ('0' <= ch <= '9'):
            return True
        else:
            return False