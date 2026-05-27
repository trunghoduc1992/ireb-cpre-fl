---
layout: page
---

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vitepress'

onMounted(() => {
  const router = useRouter()
  router.go('/')
})
</script>

# Redirecting to latest version...

You are being redirected to the [latest version (v3.3.0)](/).
