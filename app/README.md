# LeetCode Practice Desktop App

A Tauri + React desktop application for practicing LeetCode problems.

## Features

- **Problem Browser**: Tree-based navigation organized by pattern and difficulty
- **Monaco Editor**: Full-featured code editor with Python syntax highlighting
- **Auto-Save**: Changes are automatically saved after 1.5 seconds of inactivity
- **Integrated Test Runner**: Run pytest tests directly from the app
- **Collapsible Sections**: Problem definition, hints, solution, and explanation

## Development

### Prerequisites

- [Node.js](https://nodejs.org/) (v18+)
- [Rust](https://www.rust-lang.org/tools/install)
- [Python](https://www.python.org/) (for running tests)

### Setup

```bash
cd app
npm install
```

### Run in Development Mode

```bash
npm run tauri dev
```

### Build for Production

```bash
npm run tauri build
```

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+S` / `Cmd+S` | Save solution |
| `Ctrl+Enter` / `Cmd+Enter` | Run tests |

## Project Structure

```
app/
├── src/                    # React frontend
│   ├── components/         # UI components
│   │   ├── layout/         # App layout (panels, sidebar)
│   │   ├── tree/           # Problem tree navigation
│   │   ├── problem/        # Problem viewer sections
│   │   ├── editor/         # Monaco code editor
│   │   ├── test-runner/    # Test results display
│   │   └── ui/             # Reusable UI components
│   ├── hooks/              # Custom React hooks
│   ├── store/              # Zustand state stores
│   ├── lib/                # Utilities and Tauri commands
│   └── types/              # TypeScript type definitions
└── src-tauri/              # Rust backend
    └── src/
        ├── commands/       # Tauri command handlers
        └── models/         # Data structures
```
