class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        
        for c in emails:
            local, domain = c.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            c = local + "@" + domain
            res.add(c)
            
        return len(res)