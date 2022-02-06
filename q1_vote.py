import math

def get_power_of(x, y):
  return x**y

def get_mod_of(x, y):
  return x % y

def lowest_common_multiple(x, y):
  return x * y // math.gcd(x, y)

def powermod(x, y, z):
  if y == 0:
    return 1
  if y == 1:
    return x % z
  if y % 2 == 0:
    return powermod(x, y // 2, z) ** 2 % z
  else:
    return (x * powermod(x, y - 1, z)) % z

def calculate_c1_or_c2(g, m, n, r):
  g_power_m = get_power_of(g, m)
  first_mod = get_mod_of(g_power_m, get_power_of(n, 2))
  second_mod = get_mod_of(get_power_of(r, n), get_power_of(n, 2))
  mods_multiplied = first_mod * second_mod
  return get_mod_of(mods_multiplied, get_power_of(n, 2))

def decrypt(c, lam, n_sqr, mu, n):
  print('Running decryption...')
  u = c ** lam % n_sqr
  print('u', u)
  l_u = (u - 1) / n
  print('l_u', l_u)
  m = l_u * mu % n
  return m

def convert_int_to_12_bit_binary(x):
  print('Converting to 12 bit binary...')
  binary = ''
  while x > 0:
    binary = str(x % 2) + binary
    x = x // 2
  print('Binary:', binary)
  while len(binary) < 12:
    binary = '0' + binary
  print('Binary:', binary)
  return binary

def split_binary_into_4_bits(binary):
  print('')
  print('Splitting binary into 4 bits...')
  first_four = binary[:4]
  second_four = binary[4:8]
  third_four = binary[8:12]
  return first_four, second_four, third_four

def convert_float_to_integer(x):
  return int(x)

def convert_4_bit_binary_to_int(binary):
  return int(binary, 2)

def compare_vote_numbers(alice, bob, eve):
  if alice > bob and alice > eve:
    print('Alice wins!')
  elif bob > alice and bob > eve:
    print('Bob wins!')
  elif eve > alice and eve > bob:
    print('Eve wins!')
  else:
    print('Tie!')

def main():
  m1 = 1
  m2 = 1
  m3 = 1
  m4 = 1
  m5 = 16
  m6 = 16
  m7 = 256
  m8 = 256

  p = 157
  q = 127
  n = p * q
  g = 8821

  r1 = 91
  r2 = 92
  r3 = 93
  r4 = 94
  r5 = 95
  r6 = 96
  r7 = 97
  r8 = 98

  lam = lowest_common_multiple(p - 1, q - 1)
  print('lam', lam)
  u = powermod(g, lam, n ** 2)
  print('u', u)
  k = (u - 1) / n
  print('k', k)
  mu = 19261
  print('')
  print('Encrypting...')

  c1 = calculate_c1_or_c2(g, m1, n, r1)
  print('C1:', c1)
  c2 = calculate_c1_or_c2(g, m2, n, r2)
  print('C2:', c2)
  c3 = calculate_c1_or_c2(g, m3, n, r3)
  print('C3:', c3)
  c4 = calculate_c1_or_c2(g, m4, n, r4)
  print('c4:', c4)
  c5 = calculate_c1_or_c2(g, m5, n, r5)
  print('c5:', c5)
  c6 = calculate_c1_or_c2(g, m6, n, r6)
  print('c6:', c6)
  c7 = calculate_c1_or_c2(g, m7, n, r7)
  print('c7:', c7)
  c8 = calculate_c1_or_c2(g, m8, n, r8)
  print('c8:', c8)
  c = get_mod_of(c1 * c2 * c3 * c4 * c5 * c6 * c7 * c8, get_power_of(n, 2))
  print("Encryption (C) = ", c)

  print('')
  print('Decrypting...')
  decrypted = decrypt(c, lam, get_power_of(n, 2), mu, n)
  print('Decryption = ', decrypted)
  ms_added = m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8
  print('Ms added up:', ms_added)

  print('')
  if decrypted == ms_added:
    print('Decryption successful!')
  else:
    print('Decryption failed.')
    return

  print('')
  decrypted = convert_float_to_integer(decrypted)

  binary_vote = convert_int_to_12_bit_binary(decrypted)

  print(split_binary_into_4_bits(binary_vote))

  alice_votes = convert_4_bit_binary_to_int(split_binary_into_4_bits(binary_vote)[2])
  bob_votes = convert_4_bit_binary_to_int(split_binary_into_4_bits(binary_vote)[1])
  eve_votes = convert_4_bit_binary_to_int(split_binary_into_4_bits(binary_vote)[0])

  compare_vote_numbers(alice_votes, bob_votes, eve_votes)
  return

# Start program
main()
