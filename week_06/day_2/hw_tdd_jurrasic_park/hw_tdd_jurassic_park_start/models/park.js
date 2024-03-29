const Park = function (name, ticketPrice, dinosaurs = []) {
    this.name = name;
    this.ticketPrice = ticketPrice;
    this.dinosaurs = dinosaurs
  }
  
  Park.prototype.addDino = function(dino){
    this.dinosaurs.push(dino)
  }
  
  Park.prototype.removeDino = function(dino){
    const indexOfDinosaur = this.dinosaurs.indexOf(dino);
    this.dinosaurs.splice(indexOfDinosaur, 1)
  }
  
  Park.prototype.mostPopular = function(){
    let popularity = 0 
    let selectedDino
    for (dino of this.dinosaurs){
        if (dino.guestsAttractedPerDay > popularity){
            popularity = dino.guestsAttractedPerDay
            selectedDino = dino
        }
    }
    return selectedDino
  }

  module.exports = Park;
  