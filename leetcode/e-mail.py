# Every email consists of a local name and a domain name, separated by the @ sign.
#
# For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.
#
# Besides lowercase letters, these emails may contain '.'s or '+'s.
#
# If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)
#
# If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)
#
# It is possible to use both of these rules at the same time.
#
# Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails?
#
#
#
# Example 1:
#
# Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails


def numUniqueEmails(emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        final_emails = []
        for email in emails:
            before_a, after_a = email.split("@")
            before_a = before_a.replace(".", "")
            if before_a.find("+") != -1:
                before_a = before_a[:before_a.find("+")]
            print before_a, after_a
            if before_a + '@' + after_a not in final_emails:
                final_emails.append(before_a + '@' + after_a)
        return len(final_emails)

print numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
# print numUniqueEmails(["test.email+alex@leetcode.com","test.email.leet+alex@code.com"])
# print numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"])
# print numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
