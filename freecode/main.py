# This entrypoint file to be used in development. Start by reading README.md
from freecode import arithmentic_arranger_final
from unittest import main


print(arithmentic_arranger_final(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))


# Run unit tests automatically
main(module='test_module', exit=False)