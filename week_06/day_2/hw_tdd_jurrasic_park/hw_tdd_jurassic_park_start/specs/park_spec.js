const assert = require('assert');
const Park = require('../models/park.js');
const Dinosaur = require('../models/dinosaur.js');

describe('Park', function() {
  let park
  let trex
  let raptor
  let stego

  beforeEach(function () {
    park = new Park('dino world', 25, [trex, raptor]);
    trex = new Dinosaur('trex', 'carnivore', 100);
    raptor = new Dinosaur('raptor', 'carnivore', 150);
    stego = new Dinosaur('stego', 'herbivore', 2);
  })

  it('should have a name', function(){
    const actual = park.name
    assert.strictEqual(actual, 'dino world')
  });

  it('should have a ticket price', function(){
    const actual = park.ticketPrice
    assert.strictEqual(actual, 25)
  }); 

  it('should have a collection of dinosaurs', function(){
    const actual = park.dinosaurs.length
    assert.strictEqual(actual, 2)
  }); 

  it('should be able to add a dinosaur to its collection', function(){
    park.addDino(stego)
    const actual = park.dinosaurs.length
    assert.strictEqual(actual, 3)
  }); 
  
  it('should be able to remove a dinosaur from its collection', function (){
    park.removeDino(raptor)
    const actual = park.dinosaurs.length
    assert.strictEqual(actual, 1)
  });

  it('should be able to find the dinosaur that attracts the most visitors', function(){
    const actual = park.mostPopular()
    assert.deepStrictEqual(actual, raptor)
  });

  it('should be able to find all dinosaurs of a particular species');

  it('should be able to calculate the total number of visitors per day');

  it('should be able to calculate the total number of visitors per year');

  it('should be able to calculate total revenue for one year');

})