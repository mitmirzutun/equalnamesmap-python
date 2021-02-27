# equalnamesmap-python
The run generator in the main module does everything
## Input
This repo is there for getting the plazas and streets in Munich. The sorces are https://de.wikipedia.org/wiki/Liste_der_Pl%C3%A4tze_in_M%C3%BCnchen (plazas) and https://de.wikipedia.org/wiki/Liste_M%C3%BCnchner_Stra%C3%9Fennamen (streets)
## Output
Two different dictionary types will be returned. Both types have three keys in common, 'type', 'url' and 'Name'. The 'name' key will be the name of the plaza or street it extracts and the 'url' key will be the path relative to the German Wikipedia. As not every street and plaza has a Wikipedia article, it does not appear in every dictionary
### Type plaza
The 'type' key will be set to 'plaza'

The 'url' key will be the url to the plaza relative to the German Wikipedia. As not all have articles in Wikipedia, it does not exist in every plaza dictionary

The 'Pos' key will return a geohack.toolforge.org link

The 'Stadtbezirk' key will be the municipality the plaza is located at

The 'Namensherkunkft' key will contain something about the origin of the name of the plaza in German

The 'Jahr' key will contain the year the plaza got its name
### Type street
The 'type' key will be set to 'street'

The 'Historische Straße' key will be true if it is a historical street that does not exist anymore

The 'Stadtbezirk' key will be the municipality of the street. As there are historical streets, not every street has a municipality

The 'Jahr(e)' key will be the year it got the name (non historical streets) or the year range it had its name (historical street) 
