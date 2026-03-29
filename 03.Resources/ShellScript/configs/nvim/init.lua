-- ==========================================
-- 1. 기본 UI 및 줄 번호 설정
-- ==========================================
vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.cursorline = true
vim.opt.termguicolors = true

-- ==========================================
-- 2. 들여쓰기 설정
-- ==========================================
vim.opt.tabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = true
vim.opt.smartindent = true

-- ==========================================
-- 3. 검색 설정
-- ==========================================
vim.opt.ignorecase = true
vim.opt.smartcase = true
vim.opt.hlsearch = false

-- ==========================================
-- 4. 시스템 연동
-- ==========================================
vim.opt.clipboard = "unnamedplus"
vim.opt.mouse = "a"
vim.opt.runtimepath:append(vim.fn.stdpath("data") .. "/site")

-- ==========================================
-- 5. 리더 키
-- ==========================================
vim.g.mapleader = " "
vim.g.maplocalleader = " "

-- ==========================================
-- 6. 플러그인 매니저 (lazy.nvim) 자동 설치
-- ==========================================
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git", "clone", "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable", lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

-- ==========================================
-- 7. 플러그인 목록
-- ==========================================
require("lazy").setup({

  -- [1] 하단 상태 표시줄
  {
    'nvim-lualine/lualine.nvim',
    dependencies = { 'nvim-tree/nvim-web-devicons' },
    config = function()
      require('lualine').setup()
    end
  },

  -- [2] 색상 테마 (Catppuccin Mocha + 투명 배경)
  {
    "catppuccin/nvim", name = "catppuccin", priority = 1000,
    config = function()
      require("catppuccin").setup({
        flavour = "mocha",
        transparent_background = true,
        term_colors = true,
      })
      vim.cmd.colorscheme "catppuccin"
    end
  },

  -- [3] 파일 탐색기
  {
    "nvim-tree/nvim-tree.lua", version = "*", lazy = false,
    dependencies = { "nvim-tree/nvim-web-devicons" },
    config = function()
      require("nvim-tree").setup {}
      vim.keymap.set('n', '<leader>e', ':NvimTreeToggle<CR>', { noremap = true, silent = true })
    end,
  },

  -- [4] 코드 구문 강조 (Treesitter)
  {
    "nvim-treesitter/nvim-treesitter", build = ":TSUpdate",
    config = function()
      require("nvim-treesitter").setup({
        ensure_installed = {
          "c", "lua", "vim", "vimdoc", "query",
          "python", "javascript", "typescript", "html", "css", "json",
          "kotlin", "php", "java"
        },
        auto_install = true,
        highlight = { enable = true, additional_vim_regex_highlighting = false },
      })
    end,
  },

  -- [5] 파일/텍스트 검색 (Telescope)
  {
    "nvim-telescope/telescope.nvim",
    dependencies = { "nvim-lua/plenary.nvim" },
    config = function()
      local builtin = require('telescope.builtin')
      vim.keymap.set('n', '<leader>ff', builtin.find_files, { desc = '파일 찾기' })
      vim.keymap.set('n', '<leader>fg', builtin.live_grep, { desc = '텍스트 검색' })
      vim.keymap.set('n', '<leader>fb', builtin.buffers, { desc = '열려있는 파일' })
    end,
  },

  -- [6] LSP 및 자동 완성
  {
    "neovim/nvim-lspconfig",
    dependencies = {
      "williamboman/mason.nvim",
      "williamboman/mason-lspconfig.nvim",
      "hrsh7th/nvim-cmp",
      "hrsh7th/cmp-nvim-lsp",
      "hrsh7th/cmp-buffer",
      "hrsh7th/cmp-path",
      "saadparwaiz1/cmp_luasnip",
      "L3MON4D3/LuaSnip",
      "rafamadriz/friendly-snippets",
    },
    config = function()
      require("mason").setup()
      local servers = { "lua_ls", "ts_ls", "jdtls", "kotlin_language_server", "intelephense", "marksman" }
      require("mason-lspconfig").setup({ ensure_installed = servers })

      local capabilities = require("cmp_nvim_lsp").default_capabilities()
      for _, server in ipairs(servers) do
        vim.lsp.config(server, { capabilities = capabilities })
        vim.lsp.enable(server)
      end

      require("luasnip.loaders.from_vscode").lazy_load()

      local cmp = require("cmp")
      cmp.setup({
        snippet = { expand = function(args) require('luasnip').lsp_expand(args.body) end },
        mapping = cmp.mapping.preset.insert({
          ['<C-Space>'] = cmp.mapping.complete(),
          ['<CR>'] = cmp.mapping.confirm({ select = true }),
          ['<Tab>'] = cmp.mapping.select_next_item(),
          ['<S-Tab>'] = cmp.mapping.select_prev_item(),
        }),
        sources = cmp.config.sources({
          { name = 'nvim_lsp' },
          { name = 'luasnip' },
          { name = 'buffer' },
          { name = 'path' },
        })
      })
    end,
  },

  -- [7] 바이브 코딩 - tmux 창으로 텍스트 전송
  {
    "jpalardy/vim-slime",
    init = function()
      vim.g.slime_target = "tmux"
      vim.g.slime_dont_ask_default = 0
      vim.g.slime_default_config = { socket_name = "default", target_pane = "{last}" }
    end,
    config = function()
      vim.keymap.set("x", "<leader>s", "<Plug>SlimeRegionSend", { desc = "선택 영역 tmux로 전송" })
      vim.keymap.set("n", "<leader>s", "<Plug>SlimeParagraphSend", { desc = "현재 문단 tmux로 전송" })
    end,
  },
})
