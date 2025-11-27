components {
  id: "lantern"
  component: "/main/lantern.script"
}
embedded_components {
  id: "sprite"
  type: "sprite"
  data: "default_animation: \"lantern_red\"\n"
  "material: \"/builtins/materials/sprite.material\"\n"
  "textures {\n"
  "  sampler: \"texture_sampler\"\n"
  "  texture: \"/atlases/game.atlas\"\n"
  "}\n"
  ""
}
