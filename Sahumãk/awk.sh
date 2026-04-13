(
  echo "PPSA,PSA_gloss,PSA,Proto_Sahumak"
  awk -F ' => ' '
  function trim(s) {
    sub(/^[[:space:]]+/, "", s)
    sub(/[[:space:]]+$/, "", s)
    return s
  }

  NR==FNR {
    if (NF >= 2) {
      key = trim($1)
      val = trim($2)
      proto[key] = val
    }
    next
  }

  NF >= 2 {
    left = trim($1)
    psa  = trim($2)

    if (left == "" || psa == "") next

    split(left, parts, /[[:space:]]+/)
    ppsa = parts[1]
    gloss = substr(left, length(ppsa) + 2)

    print ppsa "," gloss "," psa "," proto[psa]
  }
  ' $2 $1
)