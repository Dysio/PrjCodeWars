def maskify(cc):
    return "#" * (len(cc) - 4) + ''.join(str(cc[-4:]))

print(maskify('56hg4fsdh3212345'))
