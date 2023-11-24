<template>
  <button
    class="bg-white border border-slate-100 w-52 h-14 rounded-md drop-shadow-sm space-x-1 flex flex-row items-center px-3 hover:drop-shadow transition group hover:bg-violet-500 hover:border-violet-500">
    <div class="flex flex-row gap-x-2">
      <LinkIcon class="text-violet-500 h-4 w-4 relative mt-0.5 group-hover:text-white"/>
      <div class="flex flex-col items-start">
        <span class="text-sm font-medium text-slate-700 group-hover:text-white">
          New Appointment
        </span>
        <span class="text-xs text-slate-500 group-hover:text-white">
          Ad hoc or scheduled
        </span>
      </div>
    </div>
  </button>
</template>

<script>
import { LinkIcon } from "@heroicons/vue/24/outline";

export default {
  components: {
    LinkIcon,
  }
};
</script>
