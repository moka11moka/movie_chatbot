<template>
    <v-list two-line class="pt-0 scroll-y">
        <v-toolbar flat class="search-bar">
            <v-text-field single-line hide-details placeholder="Search" prepend-inner-icon="search" color="green" class="pt-0"></v-text-field>
        </v-toolbar>
        <template v-for="(item, index) in items">
        <v-list-tile avatar active-class="grey lighten-2" :key="item.name" :value="item.selected" @click="selectItem(item)" >
            <v-list-tile-avatar size="44">
                <v-img aspect-ratio="1" :src="item.thumbnail"></v-img>
            </v-list-tile-avatar>
            <v-list-tile-content>
                <v-list-tile-title v-text="item.name"></v-list-tile-title>
                <v-list-tile-sub-title v-text="item.content"></v-list-tile-sub-title>
            </v-list-tile-content>
        </v-list-tile>
        </template>
    </v-list>
</template>


<script>

export default {
    name: "ChatContactList",
    data () {
        return {
            items: [
              { name: 'Owen', content: '完了', thumbnail: '/media/img/lrw.png', selected: true },
              { name: '三皮三皮', content: '交房租了吗？', thumbnail: '/media/img/yzb.png', selected: false },
              { name: '贻佩', content: '辣鸡', thumbnail: '/media/img/syx.png', selected: false },
              { name: 'Candice', content: '湘哥，代码写完了吗？', thumbnail: '/media/img/wj.png', selected: false },
              { name: 'FZY', content: '湘哥 你饿了吗 去吃饭吗', thumbnail: '/media/img/fzy.png', selected: false },
              { name: 'Li彡', content: '湘哥 去打球吗 我想运动下', thumbnail: '/media/img/ltc.png', selected: false },
              { name: 'Megan', content: '可以请教你问题吗', thumbnail: '/media/img/jgl.png', selected: false },
              { name: '张小猫', content: '你作业交了吗？', thumbnail: '/media/img/zzl.png', selected: false },
            ],
            selectedItem: {}
        }
    },
    mounted: function(){
        if(this.items.length > 0){
            this.selectedItem = this.items[0];
            this.$emit('selected', this.items[0]);
        }
    },
    methods: {
        selectItem: function(item){
            this.$set(this.selectedItem, 'selected', false);
            this.$set(item, 'selected', true);
            this.selectedItem = item;
            this.$emit("selected", item);
        }
    }
}

</script>