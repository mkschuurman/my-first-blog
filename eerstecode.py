deelnemer={'naam':'Mieke','werkgever':'Hanze'}
len(deelnemer)

#def hoi():
#    print('Goedendag code girls!')
#    print('Hoe gaat het?')
#hoi()

# def hoi(naam):
#    if naam == 'Mieke':
#        print('Hallo Mieke')
#    elif naam == 'Jan':
#        print ('Hoi lieve Jan')
#    else:
#        print('Dag mens zonder naam')
#
# hoi("Jan")

def hallo(naam):
    print('Hallo ' + naam + '!')

djangoteam = ['Annemarleen','Saskia', 'Sigrid', 'me']
for naam in djangoteam:
    hallo(naam)
    print('volgende')
