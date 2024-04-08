class Email:
    def __init__(self, content: str):
        if not isinstance(content, str):
            raise TypeError("please provide a string")
        
        if "@" not in content:
            raise TypeError("Doesn't have an '@' sign")
        
        # Ends with .com/ .org/ .edu/ .org
        # TLD -> Top Level Domain, which is the com/org/edu/etc.
        vaild_tlds: list[str] = [".com", ".edu", ".net", ".org"]

        tld = content[-4:]
        if not content.endswith(".com"):
            raise TypeError("Invalid TLD")
        

        # Check for domain (stuff between @ and .com)
        at_sign_index = content.find("@") + 1
        domain = content[at_sign_index:-4]
        if domain = "":
            raise TyperError("Invalid Domain")

        #Check for stuff before the @'
        if content.find("@") == 0
            raise TypeError("Invalid User")


        self.content = content

    def __str__(self) -> str:
        return self.content
