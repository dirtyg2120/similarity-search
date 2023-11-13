export q_from_user="We have appealed to their native justice"
# Cho viec debug va testing nen ko the chay tren toan bo /input dc. Chi check duoc similarity tren 1 file
echo $q_from_user
cat input/00001.txt | python3 inverted_index_mapper.py | python3 inverted_index_reducer.py | python3 jpii_mapper.py | python3 jpii_reducer.py
