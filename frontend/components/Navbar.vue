<template>
  <div class="sticky top-0 z-40 flex justify-between w-full px-6 bg-white border-b border-slate-100 divide-slate-100 navigation h-12 items-stretch">
    <div class="flex flex-row">
      <div class="border-r border-slate-100 border-solid pr-4 flex items-center">
        <div class="border-r border-slate-100 border-solid pr-4 flex items-center">
          <span>Track.</span>
        </div>
      </div>
      <div class="border-r border-slate-100 px-4 flex flex-row align-middle items-center gap-x-3 text-sm text-slate-500">
        <div class="flex flex-row gap-x-1">
          <button class="h-6 w-6 hover:bg-slate-100 rounded items-center flex flex-row justify-center hover:text-slate-900 transition duration-100">
            <ArrowLeftIcon class="h-4 w-4"/>
          </button>
          <button class="h-6 w-6 hover:bg-slate-100 rounded items-center flex flex-row justify-center hover:text-slate-900 transition duration-100">
            <ArrowRightIcon class="h-4 w-4"/>
          </button>
        </div>
        <div class="relative">
          <button class="h-6 w-6 hover:bg-slate-100 rounded items-center flex flex-row justify-center hover:text-slate-900 transition duration-100">
            <ClockIcon class="h-4 w-4"/>
          </button>
        </div>
        <div class="flex flex-row items-center relative gap-x-2 border-r border-slate-100 px-2">
          <div class="flex flex-row items-center group">
            <SunIcon class="text-yellow-400 mr-1 h-4 w-4" /> 
            <div>Today</div>
          </div>
        </div>
      </div>
    </div>
    <div class="flex flex-row items-stretch">
    </div>
  </div>
</template>
<script>
import { ArrowLeftIcon } from "@heroicons/vue/24/solid";
import { ArrowRightIcon } from "@heroicons/vue/24/solid";
import { ClockIcon } from "@heroicons/vue/24/outline";
import { SunIcon } from "@heroicons/vue/24/outline";

export default {
  components: {
    ArrowLeftIcon,
    ArrowRightIcon,
    ClockIcon,
    SunIcon,
  }
};
</script>
