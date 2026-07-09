# Configurar stats automáticas (GitHub Actions)

O perfil neofetch atualiza os números do GitHub (repos, stars, commits, followers, linhas de código) diariamente via [`.github/workflows/build.yaml`](.github/workflows/build.yaml).

## 1. Criar Personal Access Token

### Opção A — Fine-grained (recomendado)

1. Abre [GitHub Settings → Developer settings → Personal access tokens → Fine-grained tokens](https://github.com/settings/personal-access-tokens/new)
2. **Repository access:** Only select repositories → `JoaoOliveira2001`
3. **Permissions:**
   - Account: `Followers` (read), `Starring` (read)
   - Repository: `Contents` (read), `Metadata` (read), `Commit statuses` (read)
4. Gera o token e copia-o (só aparece uma vez)

### Opção B — Classic

1. Abre [Tokens (classic)](https://github.com/settings/tokens/new)
2. Scopes: `repo` (para incluir repos privados nas stats de LOC/commits)
3. Gera e copia o token

## 2. Adicionar secrets no repositório

1. Vai a `https://github.com/JoaoOliveira2001/JoaoOliveira2001/settings/secrets/actions`
2. Cria dois secrets:

| Nome | Valor |
|------|-------|
| `ACCESS_TOKEN` | O PAT que criaste |
| `USER_NAME` | `JoaoOliveira2001` |

## 3. Ativar e correr o workflow

1. **Actions** → **README build** → **Enable workflow** (se pedido)
2. **Run workflow** → branch `main` → Run
3. Aguarda ~1–3 min (primeira execução sem cache pode demorar mais)
4. Confirma em `https://github.com/JoaoOliveira2001` que o cartão aparece e os números batem certo

## 4. Atualizar retrato ASCII (opcional)

Se mudares a foto de perfil no GitHub:

```bash
curl -sL "https://avatars.githubusercontent.com/u/182710326?v=4" -o assets/portrait.jpg
python3 scripts/build_svgs.py
# Depois corre today.py localmente ou dispara o workflow
```

## Troubleshooting

- **Workflow falha com 401/403:** token expirado ou scopes insuficientes — recria o PAT
- **LOC a zero:** primeira corrida pode precisar de cache; corre de novo após a primeira execução bem-sucedida
- **Push bloqueado no workflow:** em Settings → Actions → General, permite que workflows façam push para `main`

Baseado no projeto [Andrew6rant/Andrew6rant](https://github.com/Andrew6rant/Andrew6rant).
