function one(){
    console.log('a');
    return {
      get p() {
        console.log('e');
        return {
          valueOf: function(){
            console.log('g');
            return {};
          },
          toString: function(){
            console.log('h');
            return false;
          }
        };
      },
      set p(x) {
        console.log('k');
      }
    };
  }
  