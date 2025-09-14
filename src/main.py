from match.dfa import matchStringToDfa
from parsing.dfa import loadDfaFromFile
from utils.argument_parsing import parseLexerArgs
from utils.character_parsing import regexToStandarizeRegex
from utils.file_parsing import fileReader

if __name__ == "__main__":

    parse_arguments = parseLexerArgs();

    lines:list[str] = fileReader(parse_arguments.gramatics_file); 

    dfa = loadDfaFromFile("files/gramatic-dfa.json")
    
    for line in lines:
        line = regexToStandarizeRegex(line)
        print(matchStringToDfa(dfa, line))
 



