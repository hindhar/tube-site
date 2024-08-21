def get_tube_stops():
    tube_stops = [
        "Acton Town", "Aldgate", "Aldgate East", "Alperton", "Amersham", "Angel", "Archway", 
        "Arnos Grove", "Arsenal", "Baker Street", "Balham", "Bank", "Barbican", "Barking", 
        "Barkingside", "Barons Court", "Battersea Power Station", "Bayswater", "Becontree", 
        "Belsize Park", "Bermondsey", "Bethnal Green", "Blackfriars", "Blackhorse Road", 
        "Bond Street", "Borough", "Boston Manor", "Bounds Green", "Bow Road", "Brent Cross", 
        "Brixton", "Bromley-by-Bow", "Buckhurst Hill", "Burnt Oak", "Caledonian Road", 
        "Camden Town", "Canada Water", "Canary Wharf", "Canning Town", "Cannon Street", 
        "Canons Park", "Chalfont & Latimer", "Chalk Farm", "Chancery Lane", "Charing Cross", 
        "Chesham", "Chigwell", "Chiswick Park", "Chorleywood", "Clapham Common", 
        "Clapham North", "Clapham South", "Cockfosters", "Colindale", "Colliers Wood", 
        "Covent Garden", "Croxley", "Dagenham East", "Dagenham Heathway", "Debden", 
        "Dollis Hill", "Ealing Broadway", "Ealing Common", "Earl's Court", "East Acton", 
        "East Finchley", "East Ham", "East Putney", "Eastcote", "Edgware", "Edgware Road", 
        "Elephant & Castle", "Elm Park", "Embankment", "Epping", "Euston", "Euston Square", 
        "Fairlop", "Farringdon", "Finchley Central", "Finchley Road", "Finsbury Park", 
        "Fulham Broadway", "Gallions Reach", "Gloucester Road", "Golders Green", 
        "Goldhawk Road", "Goodge Street", "Grange Hill", "Great Portland Street", "Green Park", 
        "Greenford", "Gunnersbury", "Hainault", "Hammersmith", "Hampstead", "Hanger Lane", 
        "Harlesden", "Harrow & Wealdstone", "Harrow-on-the-Hill", "Hatton Cross", 
        "Heathrow Terminals 1, 2, 3", "Heathrow Terminal 4", "Heathrow Terminal 5", 
        "Hendon Central", "High Barnet", "High Street Kensington", "Highbury & Islington", 
        "Hillingdon", "Holborn", "Holland Park", "Holloway Road", "Hornchurch", "Hounslow Central", 
        "Hounslow East", "Hounslow West", "Hyde Park Corner", "Ickenham", "Kennington", 
        "Kensal Green", "Kensington (Olympia)", "Kentish Town", "Kenton", "Kew Gardens", 
        "Kilburn", "Kilburn Park", "King's Cross St. Pancras", "Kingsbury", "Knightsbridge", 
        "Ladbroke Grove", "Lambeth North", "Lancaster Gate", "Latimer Road", "Leicester Square", 
        "Leyton", "Leytonstone", "Limehouse", "Liverpool Street", "London Bridge", "Loughton", 
        "Maida Vale", "Manor House", "Mansion House", "Marble Arch", "Marylebone", 
        "Mile End", "Mill Hill East", "Monument", "Moor Park", "Moorgate", "Morden", 
        "Mornington Crescent", "Neasden", "Newbury Park", "North Acton", "North Ealing", 
        "North Greenwich", "North Harrow", "North Wembley", "Northfields", "Northolt", 
        "Northwick Park", "Northwood", "Northwood Hills", "Notting Hill Gate", "Oakwood", 
        "Old Street", "Osterley", "Oval", "Oxford Circus", "Paddington", "Park Royal", 
        "Parsons Green", "Perivale", "Piccadilly Circus", "Pimlico", "Pinner", "Plaistow", 
        "Preston Road", "Putney Bridge", "Queen's Park", "Queensbury", "Queensway", 
        "Ravenscourt Park", "Rayners Lane", "Redbridge", "Regent's Park", "Richmond", 
        "Rickmansworth", "Roding Valley", "Rotherhithe", "Royal Oak", "Ruislip", 
        "Ruislip Gardens", "Ruislip Manor", "Russell Square", "Seven Sisters", 
        "Shadwell", "Shepherd's Bush", "Shepherd's Bush Market", "Sloane Square", 
        "Snaresbrook", "South Ealing", "South Harrow", "South Kensington", 
        "South Kenton", "South Ruislip", "South Wimbledon", "South Woodford", 
        "Southfields", "Southgate", "Southwark", "St. James's Park", "St. John's Wood", 
        "St. Paul's", "Stamford Brook", "Stanmore", "Stepney Green", "Stockwell", 
        "Stonebridge Park", "Stratford", "Sudbury Hill", "Sudbury Town", "Swiss Cottage", 
        "Temple", "Theydon Bois", "Tooting Bec", "Tooting Broadway", "Tottenham Court Road", 
        "Tottenham Hale", "Totteridge & Whetstone", "Tower Hill", "Tufnell Park", 
        "Turnham Green", "Turnpike Lane", "Upminster", "Upminster Bridge", "Upney", 
        "Upton Park", "Uxbridge", "Vauxhall", "Victoria", "Walthamstow Central", 
        "Wanstead", "Wapping", "Warren Street", "Warwick Avenue", "Waterloo", 
        "Watford", "Wembley Central", "Wembley Park", "West Acton", "West Brompton", 
        "West Finchley", "West Ham", "West Hampstead", "West Harrow", "West Kensington", 
        "West Ruislip", "Westbourne Park", "Westminster", "White City", "Whitechapel", 
        "Willesden Green", "Willesden Junction", "Wimbledon", "Wimbledon Park", "Wood Green", 
        "Woodford", "Woodside Park"
    ]
    return tube_stops

def has_no_common_letters(stop, input_text):
    stop_letters = set(stop.lower().replace(" ", ""))
    input_letters = set(input_text.lower().replace(" ", ""))
    return stop_letters.isdisjoint(input_letters)

def find_unique_stops(input_text):
    tube_stops = get_tube_stops()
    unique_stops = [stop for stop in tube_stops if has_no_common_letters(stop, input_text)]
    return unique_stops

def main():
    input_text = input("Enter any text: ")
    unique_stops = find_unique_stops(input_text)
    
    if unique_stops:
        print("Tube stops that share 0 letters with '{}':".format(input_text))
        for stop in unique_stops:
            print(stop)
    else:
        print("No tube stops share 0 letters with '{}'.".format(input_text))

if __name__ == "__main__":
    main()
