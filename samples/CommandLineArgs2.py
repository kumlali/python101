import optparse


def main():
  usage = "usage: %prog [options] arg"
  parser = optparse.OptionParser(usage)
  parser.add_option("-c", "--config", help="Configuration file")
  (options, args) = parser.parse_args()
  
  print args
  
  options.verbose
  
  if len(args) != 1:
     parser.error("incorrect number of arguments")  
  
  print options.config
  
if __name__ == "__main__":
    main()