# How do I print HiLog information of the current application only?

Use the HiLog command line tool to filter the logs of the current application.

hilog -T xxx filters logs by tag.
hilog –D xxx filters logs by domain.
hilog -e matches the log information with regular expressions and filters logs by tag, domain, and pid. Multi-layered filtering, combination filtering, and reverse filtering are supported.
