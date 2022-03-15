# Design a logger system that receives a stream of messsages along with
# their timestamps. Each unique message should only be printed at most
# every 10 seconds (i.e. a message printed at timestamp t will prevent
# other identical messages from being printed until t + 10).
#
# All messages will come in chronological order. Several messages may
# arrive at the same timestamp.
#
# Implements the Logger clas:
#   * Logger() initializes the logger object.
#   * shouldPrintMessage(timestamp, message) Returns true if the
#     message should be printed in the given timestamp, otherwise
#     returns false.

class Logger:

    def __init__(self):
        self.dictionary = {}

    def should_print_message(self, timestamp: int, message: str) -> bool:
        if message not in self.dictionary:
            self.dictionary[message] = timestamp
            return True

        if timestamp - 10 >= self.dictionary[message]:
            self.dictionary[message] = timestamp
            return True
        else:
            return False
