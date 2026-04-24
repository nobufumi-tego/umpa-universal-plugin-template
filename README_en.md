# UMPA - Universal Multilingual Plugin Architecture

A template and guide for easily and scalably creating multilingual Claude Code plugins.

**Main Concept**: Write once, scale to 10+ languages + unlimited use cases

---

## 📚 What is UMPA?

**UMPA (Universal Multilingual Plugin Architecture)** is an architecture that enables:

✅ Write your skill once in English  
✅ Support 20 languages without increasing context tokens  
✅ Add languages by adding folders only, zero code changes  
✅ Scale from 1 plugin to 1000 plugins  

### 3-Layer Architecture

```
Execution Layer (English, Claude-facing)
├── skills/
├── commands/
└── agents/
    ↓
Learning Layer (Multilingual, human-facing)
├── references/ja/
├── references/en/
├── references/zh-CN/
└── ...
    ↓
Configuration Layer
├── plugin.json
└── .mcp.json
```

**Key Insight**: The `references/` folder is NOT loaded in Claude's context. Adding languages costs zero tokens.

---

## 📁 Repository Structure

```
umpa-universal-plugin-template/
│
├── docs/
│   └── SPECIFICATION.md              ← Complete specification
│
├── template/                         ← Universal template
│   ├── .claude-plugin/
│   │   └── plugin.json
│   ├── skills/
│   │   └── example-skill/
│   │       └── SKILL.md
│   ├── commands/ (optional)
│   ├── references/
│   │   ├── ja/
│   │   │   ├── README.md
│   │   │   ├── 01-concept.md
│   │   │   ├── 02-step-by-step.md
│   │   │   ├── 03-case-studies.md
│   │   │   └── 04-advanced.md
│   │   └── en/
│   │       └── (same structure)
│   └── README.md
│
├── examples/                         ← Fully working implementations
│   ├── lean-canvas-plugin/
│   │   └── (complete plugin)
│   └── code-generator-plugin/
│       └── (complete plugin)
│
├── tools/                            ← Development tools
│   ├── add-language.sh              ← Add language script
│   └── validate-plugin.py           ← Validation tool
│
├── README.md                         ← Japanese version
├── README_en.md                      ← This file
├── LICENSE
└── .github/
    └── ISSUE_TEMPLATE/
```

---

## 🚀 Quick Start

### 1. Copy the Template

```bash
# Clone the repository
git clone https://github.com/ynobufumi/umpa-universal-plugin-template.git
cd umpa-universal-plugin-template

# Copy and customize the template
cp -r template my-awesome-plugin
cd my-awesome-plugin
```

### 2. Update Plugin Information

Edit `.claude-plugin/plugin.json`:

```json
{
  "name": "my-awesome-plugin",
  "description": "My awesome plugin description",
  "author": {
    "name": "Your Name",
    "email": "you@example.com"
  }
}
```

### 3. Create Your Skill

Add a new skill to `skills/`:

```bash
mkdir skills/my-skill
vim skills/my-skill/SKILL.md
```

Reference the template: `skills/example-skill/SKILL.md`

### 4. Create Learning Materials

Add multilingual materials to `references/`:

```bash
# Copy templates
cp -r references/ja references/ja
cp -r references/en references/en

# Edit the 5 files in each language folder
```

### 5. Test

```bash
claude --plugin-dir .
```

Test command:
```
/my-awesome-plugin:my-skill
```

### 6. Push to GitHub

```bash
git add .
git commit -m "Create my-awesome-plugin"
git push
```

---

## 📖 Documentation

### Architecture & Specification

- **[UMPA Complete Specification](docs/SPECIFICATION.md)** — Directory structure, file specs, best practices

### Development Guides

- **[Local Plugin Development](docs/LOCAL_SETUP.md)** — How to develop and test plugins locally
- **[Template Guide](template/README.md)** — Getting started with the template
- **[SKILL.md Template](template/skills/example-skill/SKILL.md)** — How to write skills

### Release & Maintenance Guides

- **[Plugin Release Guide](docs/PLUGIN_RELEASE.md)** — How to publish to marketplace
- **[Maintenance Guide](docs/MAINTENANCE.md)** — Bug fixes, new features, translations
- **[Contribution & Translation Guide](docs/CONTRIBUTION.md)** — How to contribute

### Implementation Examples

Learn from working implementations:

- **[Lean Canvas Plugin](examples/lean-canvas-plugin/)** — Complete working example
- **[Code Generator Plugin](examples/code-generator-plugin/)** — (Coming soon)

### Learning Materials Templates

- **[Japanese Learning Materials](template/references/ja/)** — Guide for Japanese users
- **[English Learning Materials](template/references/en/)** — Guide for English users

---

## 🛠️ Tools

Tools to streamline development:

### Language Addition Script

Easily add language support:

```bash
./tools/add-language.sh ja
```

The script automatically:
- Creates `references/ja/` folder
- Generates base files (README.md, etc.)

### Validation Tool

Validate plugin structure:

```bash
./tools/validate-plugin.py
```

Checks:
- ✅ plugin.json validity
- ✅ SKILL.md format
- ✅ references/ folder structure
- ✅ Language folder consistency

---

## 💡 How UMPA Works

### Context Efficiency

| Component | Loaded | Tokens |
|-----------|--------|--------|
| plugin.json | ✅ Yes | ~100 |
| skills/ | ✅ Yes | ~350/skill |
| commands/ | ✅ Yes | ~200 |
| references/ | ❌ No | 0 |
| scripts/ | ❌ No | 0 |
| templates/ | ❌ No | 0 |

**Initial Context**: ~1,200 tokens (fixed regardless of language count)

### Adding Languages

1. Create folder: `references/[lang]/`
2. Translate 5 files
3. Add language link to parent README
4. Commit & Push

**Impact**: Context tokens +0, Plugin size +50-100KB

---

## 🌍 Supported Languages

Languages currently included in templates:

| Language | Code | Status |
|----------|------|--------|
| 日本語 (Japanese) | ja | ✅ Complete |
| English | en | ✅ Complete |
| 简体中文 (Simplified Chinese) | zh-CN | 📝 Template |
| 繁體中文 (Traditional Chinese) | zh-TW | 📝 Template |
| 한국어 (Korean) | ko | 📝 Template |
| Español (Spanish) | es | 📝 Future |

**Template status** = Folder structure and templates are ready, but example translations are not yet implemented

---

## 📊 Scalability

UMPA scalability metrics:

| Metric | Min | Recommended | Max |
|--------|-----|-------------|-----|
| Skills per plugin | 1 | 5 | 50+ |
| Languages | 2 | 5 | 20+ |
| Initial context | ~1,200t | ~1,200t | ~1,500t |
| Time to add language | 2h | 4-6h | 8h |

**Key**: Adding skills barely changes context. Adding languages costs zero tokens.

---

## 🤝 Contributing

How to improve UMPA:

1. **Template Improvements** - Suggest via GitHub Issues
2. **New Languages** - Submit translations as PRs
3. **Implementation Examples** - Add new plugin examples
4. **Bug Reports** - Report issues on GitHub Issues
5. **Feedback** - Share your experience

---

## 📝 License

MIT License - Free to use, modify, and distribute.

See [LICENSE](LICENSE) for details.

---

## 🔗 Related Resources

- **Claude Code Official Docs**: https://code.claude.com
- **Plugin Development Guide**: https://code.claude.com/docs/plugins
- **UMPA Specification**: [docs/SPECIFICATION.md](docs/SPECIFICATION.md)

---

## 📞 Support

### FAQ

**Q: I want to support multiple languages at once**  
A: Copy the `template/references/` folder and translate the content in each language folder.

**Q: I want to migrate an existing plugin to UMPA**  
A: Check the "Migration Guide" section in the specification, or open a GitHub Issue.

**Q: I want to customize beyond language additions**  
A: Refer to the "Customization Guide" in the specification.

### Feedback

- 📧 Email: nobufumi.yoshida@tegosacloud.com
- 🐙 GitHub: [@ynobufumi](https://github.com/ynobufumi)
- 🔗 Issues: [GitHub Issues](https://github.com/ynobufumi/umpa-universal-plugin-template/issues)

---

## 🎯 Next Steps

### Plugin Development Flow

1. **Set up Local Environment** → [Local Development Guide](docs/LOCAL_SETUP.md)
   ```bash
   cp -r template my-plugin
   cd my-plugin
   claude --plugin-dir .
   ```

2. **Understand the Spec** → [UMPA Specification](docs/SPECIFICATION.md)

3. **Reference Examples** → [Lean Canvas Plugin](examples/lean-canvas-plugin/)

4. **Develop Your Plugin** → Create skills, commands, learning materials

5. **Test Locally** → `./tools/validate-plugin.py`

6. **Push to GitHub** → [Release Guide](docs/PLUGIN_RELEASE.md)

7. **Register on Marketplace** → Follow the release guide

8. **Maintain & Support** → [Maintenance Guide](docs/MAINTENANCE.md)

---

**Made with ❤️ by Nobufumi Yoshida**

Last Updated: 2026-04-24

---

[Japanese Version](README.md)
