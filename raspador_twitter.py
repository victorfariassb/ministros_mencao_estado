import twint

user_ministros = [
'damaresalves',
'Tarcisiogdf',
'fabiofaria',
'minluizramos',
'mribeiroMEC',
'JairBolsonaro',
'joaoromaneto',
'gilsonmachadont',
'andersongtorres',
'generalMourao',
'rogeriosmarinho',
'onyxlorenzoni',
'terezacrisms',
'mqueiroga2',
'astro_pontes',
'wrosarioCGU',
'flaviaarrudadf',
'gen_heleno',
'brunobiancoleal',
'ciro_nogueira',
'joaquimleitemma']

c = twint.Config()
c.Username = 'Tarcisiogdf'
c.Since = '2019-01-01'
c.Until = '2021-12-07'
c.Pandas = True
c.Store_csv = True
c.Output = "tarcisio_chuvas.csv"

twint.run.Search(c)
