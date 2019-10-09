if __name__ == "__main__":
    import sys
    import os

    print("Error: there is no module 'nichtparasoup'.", "Did you mean 'nichtparasoup-server'?",
          file=sys.stderr,
          sep=os.linesep, end=os.linesep)
    sys.exit(1)
